import pycps

# Create a connection to a Clusterpoint database.
con = pycps.Connection('tcp://cloud-us-0.clusterpoint.com:9007', 'Database1', 'r3x.asadun@live.com', '12345', '100492')

docs_mixed = { 6: {'text': 'Lorem ipsum.', 'textxxx': 'Lorem ipsum.', 'title': 'Title!'}, 2: '<document/>'}

con.insert(docs_mixed)
