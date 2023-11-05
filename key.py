import os
import openai
import time

# Load your API key from an environment variable or secret management service
openai.api_key = os.getenv("OPENAI_API_KEY")




def generate_email(community, data):
    training = open('trainingTxt.txt', 'r')
    # Define the system message
    system_msg = f"""
    You are a knowlegable leads acquisition agent specializing in client prospecting and sales, working for TerraByte Solutions. TerraByte Solutions is a web development company that draws its inspiration and ethos from the pioneering spirit of exploration that characterized Newfoundland's history. It positions itself as a bridge between traditional pioneering values ("Terra Nova") and the digital frontier ("TerraByte"). The company aims to create robust and enduring websites, which not only serve as a business's digital presence but also as a platform for growth and engagement in the online ecosystem. {training}
    """

    # Define the user message
    user_msg = f"""
        Write a professional lead acquisition email for TerraByte Solutions. The email is addressed to the Municipal Manager of {community}. Mention our services in web design and development, cybersecurity, and AI-driven solutions. Highlight our commitment to enhancing economic development, quality of living, and population growth. Our aim is to partner with them to revitalize their community's digital presence. Begin with a greeting, introduce TerraByte Solutions, provide the offer drawing on specific data points provided in the data, and end with a call to action. Here is the data: {data}
        """

    # Create a dataset using GPT
    response = openai.ChatCompletion.create(model="gpt-3.5-turbo-16k",
                                            messages=[{"role": "system", "content": system_msg},
                                            {"role": "user", "content": user_msg}])
    return response


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
        filepaths[community]=path
    return filepaths
 
# Function to read the .txt file and return structured data
def read_dataset(file_path, community):
    # Implement the logic to read the file and structure the data

    try:
        file = open(file_path, 'r')
        content = 'Data for: ' + community + '\n' + file.read()

        return content
    except:
        print(community + " not found at " + file_path)
        


# Main logic
def main():
    communities = read_communities()
    filepaths = get_filepaths(communities)
    # print(filepaths)ç

    communities_info = {}
    for key in filepaths:
        path = filepaths[key] + '/data.txt'
        communities_info[key]=read_dataset(path, key)
        # print("key: " +key)

    # Generate and print emails for each community
    for community in communities_info:
        # print(community)
        email_content = generate_email(community, communities_info[community])
        print(f"Email for {community}:\n")
        print(email_content['choices'][0]['message']['content'])
        filename = str(community) + "-email.txt"
        path = "/Users/gavin/Documents/Townfolio data/Emails/" + filename
        try:
            f = open(path, "x")
            f.write(email_content['choices'][0]['message']['content'])
            f.close()
        except:
            continue
        # print(f.read())
        print("-" * 40)

        time.sleep(1)

if __name__ == "__main__":
    main()