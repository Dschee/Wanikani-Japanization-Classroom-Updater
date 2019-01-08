from spreadsheet_handler import SpreadsheetHandler
from wk_profile_fetcher import WKProfileFetcher


def main():
    # Fetching classroom members names from spreadsheet
    classroom_spreadsheet = SpreadsheetHandler()
    profiles_names = classroom_spreadsheet.get_profile_names()
    # Fetching profile items data from WK website
    profiles_items = []
    for profile_name in profiles_names:
        profile = WKProfileFetcher(profile_name)
        profiles_items.append(profile.get_items())
    # Updating spreadsheet with new numbers
    classroom_spreadsheet.set_profiles_items(profiles_items)


if __name__ == '__main__':
    main()
