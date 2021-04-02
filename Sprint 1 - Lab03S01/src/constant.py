URL = 'https://api.github.com/graphql'
TOKEN = 'INSERT YOUR TOKEN HERE'
HEADERS = {
    'Content-Type': 'application/json',
    'Authorization': f'bearer {TOKEN}'
}
QUERY = """
{
    search(query:"stars:>100", type:REPOSITORY, first:5){
        pageInfo {
            startCursor
            endCursor
            hasNextPage
        }
        nodes {
        ... on Repository {
                nameWithOwner
                name
                url
                sshUrl
                createdAt 
                mr: pullRequests(states: MERGED){
                    totalCount
                }
                mc: pullRequests(states: CLOSED){
                    totalCount
                }
            } 
        } 
    }
}
"""
PATH_CSV = 'output_github.csv'
