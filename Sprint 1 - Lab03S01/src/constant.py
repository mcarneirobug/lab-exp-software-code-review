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
                owner {
                    login
                }
            } 
        } 
    }
}
"""
QUERY_DATA_SET = """
{
  repository(owner: "{OWNER}", name: "{REPOSITORY_NAME}") {
    merged: pullRequests(first: 2, after: null, states: MERGED) {
      totalCount
      nodes {
        createdAt
        mergedAt
        bodyText
        id
        reviews {
          totalCount
        }
        participants {
          totalCount
        }
        files {
          totalCount
        }
      }
    }
    closed: pullRequests(first: 5, after: null, states: CLOSED) {
      totalCount
      nodes {
        createdAt
        mergedAt
        bodyText
        id
        reviews {
          totalCount
        }
        participants {
          totalCount
        }
        files {
          totalCount
        }
      }
    }
  }
  rateLimit {
    remaining
  }
}
"""
PATH_CSV = 'output_github.csv'
