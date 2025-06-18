import os
import json
import shutil
import pandas as pd

class DataTransformer:
    """
    A class for extracting and transforming StatsBomb match and shot event data from JSON files.

    Attributes:
        source_metadata (str): Path to the match metadata JSON file.
        target_folder (str): Directory where the extracted event JSONs will be saved.
        source_event_data (str): Directory containing raw event JSON files.
    """

    def __init__(self, source_metadata, target_folder, source_event_data):
        self.source_metadata = source_metadata
        self.target_folder = target_folder
        self.source_event_data = source_event_data
        self.match_ids = []

    def get_match_ids(self):
        """Extract all match_ids from the tournament metadata JSON."""
        if not os.path.exists(self.source_metadata):
            raise FileNotFoundError(f"Source metadata file {self.source_metadata} not found.")

        with open(self.source_metadata, "r", encoding="utf-8") as f:
            try:
                matches = json.load(f)
                self.match_ids = [str(match["match_id"]) for match in matches]
                print(f"Found {len(self.match_ids)} matches.")
                return self.match_ids
            except json.JSONDecodeError as e:
                raise ValueError(f"Error decoding JSON from {self.source_metadata}: {e}")

    def get_match_events(self):
        """
        Copy event JSON files for the match_ids into the target folder.
        """
        os.makedirs(self.target_folder, exist_ok=True)

        for match_id in self.match_ids:
            filename = f"{match_id}.json"
            src = os.path.join(self.source_event_data, filename)
            dst = os.path.join(self.target_folder, filename)

            if os.path.exists(src):
                shutil.copy(src, dst)
            else:
                print(f"Missing {filename}, skipping...")

        print(f"Done copying event files to {self.target_folder}")
        print(f"Total files copied: {len(os.listdir(self.target_folder))}")

    def create_dataframe(self, save_path=None):
        """
        Extract shot-related events from JSON files and return them as a pandas DataFrame.

        Args:
            save_path (str, optional): Path to save the resulting CSV. If None, data won't be saved.

        Returns:
            pd.DataFrame: DataFrame containing all shot events.
        """
        all_shots = []

        for filename in os.listdir(self.target_folder):
            if filename.endswith(".json"):
                file_path = os.path.join(self.target_folder, filename)
                with open(file_path, "r", encoding="utf-8") as f:
                    try:
                        events = json.load(f)
                        for event in events:
                            if event.get("type", {}).get("name") == "Shot":
                                all_shots.append(event)
                    except json.JSONDecodeError:
                        print(f"Error decoding {filename}, skipping.")

        shots_df = pd.json_normalize(all_shots)
        print(f"Total shots found: {len(shots_df)}")

        if save_path:
            shots_df.to_csv(save_path, index=False)
            print(f"Saved shot data to: {save_path}")

        return shots_df

