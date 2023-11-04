import os
import openai

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")




def generate_email(community):
    # Define the system message
    system_msg = f"""
    You are a knowlegable leads acquisition agent specializing in client prospecting and sales, working for TerraByte Solutions. TerraByte Solutions is a web development company that draws its inspiration and ethos from the pioneering spirit of exploration that characterized Newfoundland's history. It positions itself as a bridge between traditional pioneering values ("Terra Nova") and the digital frontier ("TerraByte"). The company aims to create robust and enduring websites, which not only serve as a business's digital presence but also as a platform for growth and engagement in the online ecosystem.
    """

    # Define the user message
    user_msg = f"""
        Write a professional lead acquisition email for TerraByte Solutions. The email is addressed to the Municipal Manager of {community}. Mention our services in web design and development, cybersecurity, and AI-driven solutions. Highlight our commitment to enhancing economic development, quality of living, and population growth. Our aim is to partner with them to revitalize their community's digital presence. Begin with a greeting, introduce TerraByte Solutions, provide the offer, and end with a call to action.
        """

    # Create a dataset using GPT
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo",
                                            messages=[{"role": "system", "content": system_msg},
                                            {"role": "user", "content": user_msg}])



#Function to get list of communities in directory
def read_communities():
    communities = []
    directory = '/Users/gavin/Documents/Townfolio data/'
    for file in os.listdir(directory):
        communities.append(file)
    return communities

def get_filepaths(communities):
    filepaths= {}
    for community in communities:
        path = r'/Users/gavin/Documents/Townfolio data/' + community
        filepaths[community].append(path)
    return filepaths
 
# Function to read the .txt file and return structured data
def read_dataset(file_path, community):
    # Implement the logic to read the file and structure the data

    file = open(file_path, 'r')
    content = 'Data for: ' + community + '\n' + file.read()

    return {community: content}


# Main logic
def main():
    communities = read_communities()
    filepaths = get_filepaths(communities)
    for key in filepaths:
        path = filepaths[key] + '/data.txt'
        communities_info = {}
        communities_info. append(read_dataset(path, key))

    # Generate and print emails for each community
    for community in communities_info:
        email_content = generate_email(communities_info[community])
        print(f"Email for {community}:\n")
        print(email_content)
        print("-" * 40)