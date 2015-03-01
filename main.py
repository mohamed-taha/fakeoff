import facebook

token = 'CAAKDZBXNh5AkBALpiQ8MYlfrgDCYn9yJWGsWgP9qhmhsCsjkJUScW87kdT5kSgJBNjCtHLzrPSoy7hOmcr5Nz5fN1VyllKwdoRUs7TmZAJ9qDD9asxscZAwnH1dn1qI9UlVRxRdbguxjLeLY929h7kwynOZAs8n7iYv0BqXZA9ZAxjxrn0UHfThDnkeXUiUwatoGSYAGzb0ZBcCJFZAG6T68'

graph = facebook.GraphAPI(token)
profile = graph.get_object("me")
friends = graph.get_object("me/friends")
for friend in friends['data']:
    print "{0} has id {1}".format(friend['name'].encode('utf-8'), friend['id'])