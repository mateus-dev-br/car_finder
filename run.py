import argparse
import subprocess
import os

def seed():
    print("📦 Seeding the database...")
    subprocess.run(["python3", "app/db/seed.py"], env={**os.environ, "PYTHONPATH": "."})

def start_server():
    print("🚀 Starting the server...")
    subprocess.run(["python3", "app/server/server.py"], env={**os.environ, "PYTHONPATH": "."})

def start_agent():
    print("🤖 Launching the agent...")
    subprocess.run(["python3", "app/client/agent.py"], env={**os.environ, "PYTHONPATH": "."})

def main():
    parser = argparse.ArgumentParser(description="Car Finder Project - Command Line Runner")
    parser.add_argument(
        "command",
        choices=["seed", "server", "agent"],
        help="Choose which command to run: seed | server | agent"
    )

    args = parser.parse_args()

    if args.command == "seed":
        seed()
    elif args.command == "server":
        start_server()
    elif args.command == "agent":
        start_agent()



if __name__ == "__main__":
    main()
