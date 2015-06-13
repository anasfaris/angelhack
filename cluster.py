import pycps

def cluster():
    con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007',
                           'companies',
                           'anasfaris@yahoo.com',
                           '12345678',
                           '100455')
                
    # # Insert.
    # docs_mixed = {1: {'name': 'Celcom', 'score': '500'}, 
    #               2: {'name': 'Digi', 'score': '200'}}
    # try:
    #     con.insert(docs_mixed)
    # except pycps.APIError as e:
    #     print(e)

    response = con.lookup(['1','2'])

    for id, doc in response.get_documents().items():
        print id, doc['name']

cluster()
