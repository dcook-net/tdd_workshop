class Customer(object):
    def __init__(self, customer_id, email, firstname, lastname, gender, products):
        self.customer_id = customer_id
        self.email_address = email
        self.first_name = firstname
        self.last_name = lastname
        self.gender = gender
        self.purchased_products = products

    def __eq__(self, obj):
        return isinstance(obj, Customer) \
               and obj.customer_id == self.customer_id \
               and obj.email_address == self.email_address \
               and obj.first_name == self.first_name \
               and obj.last_name == self.last_name \
               and obj.gender == self.gender \
               and obj.purchased_products == self.purchased_products


class TargetedCustomer(object):

    def __init__(self, customer_id, email, firstname, lastname):
        self.customer_id = customer_id
        self.email = email
        self.forename = firstname
        self.surname = lastname

    def __eq__(self, obj):
        return isinstance(obj, TargetedCustomer) \
               and obj.customer_id == self.customer_id \
               and obj.email == self.email \
               and obj.forename == self.forename \
               and obj.surname == self.surname


# This is here for reference only
class RealCustomerRepository(object):

    def get_all_customers(self):
        # Real implementation omitted for
        # Connecting to DB and retrieving all customer data
        return [
            Customer(123, '', '', '', 'm', [])
        ]


class CampaignManager(object):
    def __init__(self, customer_repository, mvt_service):
        self.customer_repository = customer_repository
        self.mvt_service = mvt_service

    def get_homeowners(self):
        all_customers = self.customer_repository.get_all_customers()
        new_feature = self.mvt_service.getABTest('some_key')

        male_homeowners = []
        for customer in all_customers:
            if customer.gender == 'm' and 'home' in customer.purchased_products:
                male_homeowners.append(customer if new_feature else self.__map_customer(customer))

        return male_homeowners

    # Private function is tested implicitly, as it is called from a public function
    @staticmethod
    def __map_customer(customer):
        return TargetedCustomer(customer.customer_id,
                                customer.email_address,
                                customer.first_name,
                                customer.last_name)


class StubDataStore(object):
    def __init__(self, stubbed_data):
        self.stubbed_data = stubbed_data

    def get_all_customers(self):
        return self.stubbed_data


class StubMvtService(object):
    def __init__(self, stubbed_response):
        self.stubbed_response = stubbed_response

    def getABTest(self, key):
        return self.stubbed_response


stubbed_data = [
    Customer(12456, 'tom.thumb@test.com', 'tom', 'thumb', 'm', ['home']),
    Customer(64541, 'bob.evens@test.com', 'bob', 'evens', 'm', ['home']),
    Customer(49357, 'barry.scott@test.com', 'barry', 'scott', 'm', ['home']),

    Customer(78345, 'clair.cummings@test.com', 'clair', 'cummings', 'f', ['home']),  # not a male customer
    Customer(38764, 'harvy.eason@test.com', 'harvey', 'eason', 'm', ['car']),  # not an existing home customer
]


def test_should_return_all_male_homeowners():
    stubbed_mvt_service = StubMvtService(False)
    customer_data_store = StubDataStore(stubbed_data)
    expected = [
        TargetedCustomer(12456, 'tom.thumb@test.com', 'tom', 'thumb'),
        TargetedCustomer(64541, 'bob.evens@test.com', 'bob', 'evens'),
        TargetedCustomer(49357, 'barry.scott@test.com', 'barry', 'scott')
    ]

    campaign_manager = CampaignManager(customer_data_store, stubbed_mvt_service)

    homeowners = campaign_manager.get_homeowners()

    assert homeowners == expected


def test_should_return_full_customer_object_when_mtv_is_on():
    stubbed_mvt_service = StubMvtService(True)
    customer_data_store = StubDataStore(stubbed_data)
    expected = [
        Customer(12456, 'tom.thumb@test.com', 'tom', 'thumb', 'm', ['home']),
        Customer(64541, 'bob.evens@test.com', 'bob', 'evens', 'm', ['home']),
        Customer(49357, 'barry.scott@test.com', 'barry', 'scott', 'm', ['home'])
    ]

    campaign_manager = CampaignManager(customer_data_store, stubbed_mvt_service)

    homeowners = campaign_manager.get_homeowners()

    assert homeowners == expected
