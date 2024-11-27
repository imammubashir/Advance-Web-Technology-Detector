import requests
import os

# Function to analyze the website
def analyze_website(url):
    print(f"Analyzing the website: {url}")
    # Placeholder logic for website analysis (you can add actual analysis here)
    try:
        response = requests.get(url)
        if response.status_code == 200:
            return {
                "Server": response.headers.get("Server", "Unknown"),
                "Powered By": response.headers.get("X-Powered-By", "Unknown"),
                "Status": "Website is reachable"
            }
        else:
            return {"Status": "Website is not reachable"}
    except requests.exceptions.RequestException as e:
        return {"Error": str(e)}

# Function to detect technologies used in the website
def detect_technology(url):
    print(f"Detecting technologies used in: {url}")
    # Placeholder logic to detect technologies used in the website
    technologies = []
    # Example detection - you can add more logic to detect actual technologies
    if "wordpress" in url:
        technologies.append("WordPress")
    if "php" in url:
        technologies.append("PHP")
    return technologies

# Function to analyze WordPress features
def analyze_wordpress_features(url):
    print(f"Analyzing WordPress features for: {url}")
    # Placeholder logic to detect WordPress features (themes, plugins, etc.)
    return {
        "Themes": ["Twenty Twenty-One", "Astra"],  # Example themes
        "Plugins": ["Yoast SEO", "WooCommerce"]  # Example plugins
    }

# Function to detect PHP libraries
def detect_php_libraries(url):
    print(f"Detecting PHP libraries used in: {url}")
    # Placeholder logic for PHP libraries detection
    return ["Laravel", "Symfony"]  # Example libraries

# Function to analyze the local project directory
def detect_dependencies_in_directory(directory):
    languages = {}
    print(f"Scanning directory: {directory}")
    for root, _, files in os.walk(directory):
        for file in files:
            print(f"Checking file: {file}")
            if file.endswith(".py"):
                languages["Python"] = languages.get("Python", 0) + 1
            elif file.endswith(".js"):
                languages["JavaScript"] = languages.get("JavaScript", 0) + 1
            elif file.endswith(".php"):
                languages["PHP"] = languages.get("PHP", 0) + 1
            elif file.endswith(".html") or file.endswith(".htm"):
                languages["HTML"] = languages.get("HTML", 0) + 1
            elif file.endswith(".css"):
                languages["CSS"] = languages.get("CSS", 0) + 1
    print(f"Detected languages: {languages}")
    return languages

# Function to analyze the project (either website or local directory)
def analyze_project(url=None, directory=None):
    report = {}

    if url:
        print("Analyzing website...")
        # Step 1: Analyze website
        web_info = analyze_website(url)
        technologies = detect_technology(url)
        report["Website Info"] = web_info
        report["Technologies Detected"] = technologies
        
        # If WordPress is detected, analyze WordPress features
        if "WordPress" in technologies:
            wordpress_features = analyze_wordpress_features(url)
            report["WordPress Features"] = wordpress_features
        
        # If PHP is detected, check for libraries
        if "PHP" in technologies:
            php_libraries = detect_php_libraries(url)
            report["PHP Libraries"] = php_libraries

    if directory:
        print("Analyzing local project...")
        # Step 2: Analyze local project
        dependencies = detect_dependencies_in_directory(directory)
        report["Project Languages"] = dependencies

    return report

# Main User Interaction
if __name__ == "__main__":
    choice = input("Would you like to analyze a website or a local project directory? (website/project): ").lower()

    if choice == "website":
        url = input("Enter the website URL to analyze (e.g., https://www.example.com): ")
        analysis_report = analyze_project(url=url)
    
    elif choice == "project":
        project_dir = input("Enter the local project directory to analyze (e.g., /path/to/your/project): ")
        analysis_report = analyze_project(directory=project_dir)

    else:
        print("Invalid choice. Please choose either 'website' or 'project'.")
        exit()

    # Print the analysis report
    for section, details in analysis_report.items():
        print(f"\n--- {section} ---")
        if isinstance(details, dict):
            for key, value in details.items():
                print(f"{key}: {value}")
        else:
            print(f"{details}")
