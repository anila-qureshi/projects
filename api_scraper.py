import subprocess
import csv
import os

# List of repository URLs
repositories = [
    "https://github.com/huggingface/transformers",
    "https://github.com/Anthropic/claude",
    "https://github.com/EleutherAI/gpt-neo",
]
def results(repositories):
    # Create a CSV file to store the commit data
    csv_file = "commit_data.csv"

    # Create a CSV writer
    with open(csv_file, mode="w", newline="") as file:
        csv_writer = csv.writer(file)

        # Write header row
        csv_writer.writerow(["Repository", "Commit Hash", "Author", "Date and Time", "Commit Message", "Insertions", "Deletions"])

        # Loop through each repository
        for repo_url in repositories:
            print(repo_url) # print for my own sanity
            # Extract repository name from the URL
            repo_name = repo_url.split("/")[-1].replace(".git", "")

            # Specify the full path to the repository directory
            repo_directory = os.path.join(os.getcwd(), repo_name)

            # Clone the repository if it doesn't exist
            if not os.path.exists(repo_directory):
                subprocess.run(["git", "clone", repo_url], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Change to the repository directory
            os.chdir(repo_directory)

            # Fetch the latest changes
            subprocess.run(["git", "fetch"], stdout=subprocess.PIPE, stderr=subprocess.PIPE)

            # Get the list of all commit hashes from newest to oldest
            commit_hashes = subprocess.run(["git", "log", "--format='%H'"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
            # Get the list of all commit hashes (newest first by default)

            commit_hashes = commit_hashes.stdout.strip().split("\n")

            # Loop through each commit hash
            for hash in commit_hashes:
                hash = hash.strip("'")
                # Get commit author
                author_results = subprocess.run(["git", "log", "-n", "1", "--pretty=format:%an", hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if author_results.stderr:
                    print(f"Error getting author for commit {hash}: {author_results.stderr}")
                    continue
                author = author_results.stdout.strip()
                # print(author,len(author))  --commented out but can be used for additional testing
                
                
                # Get commit date and time
                datetime = subprocess.run(["git", "log", "-n", "1", "--pretty=format:%ad", "--date=iso", hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True).stdout.strip()
                # print(datetime, len(datetime)) --commented out but can be used for additional testing
                
                
                # Get commit message
                message = subprocess.run(["git", "log", "-n", "1", "--pretty=format:%s", hash], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                # print(message, len(message))  --commented out but can be used for additional testing
                if message.stderr:
                    print(f"Error getting message for commit {hash}: {message.stderr}")
                    continue
                message = message.stdout.strip()
                
                # Get the number of insertions and deletions
                stats = subprocess.run(["git", "diff", "--shortstat", f"{hash}^..{hash}"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True)
                if stats.stderr:
                    print(f"Error getting author for commit {hash}: {stats.stderr}")
                    continue
                stats = stats.stdout.strip()
                
                # Split the insertions and deletions from the statistics
                stats_parts = stats.split(",")
                # print(len)  --commented out but can be used for additional testing
                insertions = stats_parts[0].strip() if len(stats_parts) > 0 else "0"
                deletions = stats_parts[1].strip() if len(stats_parts) > 1 else "0"

                # Write commit data to the CSV file
                csv_writer.writerow([repo_name, hash, author, datetime, message, insertions, deletions])

            # Return to the parent directory
            os.chdir("..")
    return author, datetime, message, stats