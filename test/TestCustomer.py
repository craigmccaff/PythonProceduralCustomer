from src.Customers import *
def test_loadCustomer():
    if "emailAddress" == loadCustomers()[0][0]:
        print("Pass","test_loadCustomer")
    else:
        print("fail", "test_loadCustomer")

def main():
    test_loadCustomer()

if __name__ == '__main__':
    main()
