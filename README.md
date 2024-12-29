# ObsidianBrain

ObsidianBrain 🧠

A local AI-powered chatbot plugin for Obsidian that enhances note management, provides intelligent summaries, and visualizes relationships between your ideas.

📖 Table of Contents
	1.	Introduction
	2.	Features
	3.	Installation
	4.	Usage
	5.	Configuration
	6.	Contributing
	7.	License

✨ Introduction

ObsidianBrain is a cutting-edge Obsidian plugin designed for knowledge enthusiasts and productivity seekers. By leveraging local AI models, it empowers users to manage and analyze their notes more effectively, discover hidden connections, and generate insights with ease. All features run offline, ensuring privacy and security.

🌟 Features
	•	Local AI Querying: Ask questions about your notes and get instant, AI-driven answers.
	•	Note Summarization: Automatically create summaries for your notes.
	•	Relationship Visualization: Identify and display connections between related notes.
	•	Offline Operation: Fully functional without requiring an internet connection.
	•	Customizable AI: Choose your own AI model or integrate external APIs.

🔧 Installation

Prerequisites
	•	Obsidian (latest version)
	•	Python 3.8 or higher
	•	Pre-trained local AI model (e.g., LLaMA 2, GPT-4 All)

Steps
	1.	Clone the repository:

git clone https://github.com/yourusername/ObsidianBrain.git
cd ObsidianBrain


	2.	Install Python dependencies:

pip install -r requirements.txt


	3.	Place your pre-trained model in the models/ directory.
	4.	Enable the plugin in Obsidian:
	•	Go to Settings > Community Plugins > Install Plugin.
	•	Load the plugin folder or use the manual installation guide.

🛠️ Usage
	1.	Activate the plugin in Obsidian settings.
	2.	Access the following commands via the command palette (Ctrl/Cmd + P):
	•	“Ask ObsidianBrain”: Query your notes.
	•	“Summarize Note”: Generate a concise summary of the current note.
	•	“Visualize Relationships”: See a graph of related notes.
	3.	Customize the plugin settings in the config.yaml file located in the plugin folder.

⚙️ Configuration

You can adjust the plugin settings by modifying the config.yaml file:

model_path: models/llama-2-7b.bin
max_tokens: 512
temperature: 0.7
api_key: null

	•	model_path: Path to your local AI model.
	•	max_tokens: Maximum number of tokens for query responses.
	•	temperature: Controls response randomness (higher = more creative).
	•	api_key: Optional; used for integrating external AI services.

🤝 Contributing

We welcome contributions to make ObsidianBrain even better! Here’s how you can get involved:
	1.	Fork the repository.
	2.	Create a branch for your feature or bugfix:

git checkout -b feature-name


	3.	Commit and push your changes:

git commit -m "Add feature XYZ"
git push origin feature-name


	4.	Open a pull request on GitHub.

Check out the CONTRIBUTING.md file for more details.

📜 License

This project is licensed under the Apache License 2.0.
You can read the full license in the LICENSE file.

🚀 Future Plans
	•	Cloud-based AI integration for fallback support.
	•	Advanced graph visualization for note relationships.
	•	Enhanced user interface for non-technical users.

💬 Feedback

Have feedback or questions? Open an issue or contact us at xistoh162108@kaist.ac.kr. We’d love to hear from you!

Example Screenshot

(Include a screenshot or GIF demonstrating the plugin in action.)
