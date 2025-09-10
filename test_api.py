#!/usr/bin/env python3
"""
Simple test script to verify the SBM API endpoints
Run this after starting the Django development server
"""

import requests
import json
import time

BASE_URL = "http://127.0.0.1:8000"

def test_items_api():
    """Test the Items CRUD API"""
    print("Testing Items API...")
    
    # Test creating an item
    item_data = {
        "name": "Test Item",
        "description": "This is a test item created by the test script"
    }
    
    try:
        response = requests.post(f"{BASE_URL}/api/items/", json=item_data)
        if response.status_code == 201:
            print("✓ Item created successfully")
            item = response.json()
            item_id = item['id']
        else:
            print(f"✗ Failed to create item: {response.status_code}")
            return False
    except Exception as e:
        print(f"✗ Error creating item: {e}")
        return False
    
    # Test getting all items
    try:
        response = requests.get(f"{BASE_URL}/api/items/")
        if response.status_code == 200:
            print("✓ Items retrieved successfully")
        else:
            print(f"✗ Failed to get items: {response.status_code}")
    except Exception as e:
        print(f"✗ Error getting items: {e}")
    
    # Test updating the item
    update_data = {
        "name": "Updated Test Item",
        "description": "This item has been updated"
    }
    
    try:
        response = requests.put(f"{BASE_URL}/api/items/{item_id}/", json=update_data)
        if response.status_code == 200:
            print("✓ Item updated successfully")
        else:
            print(f"✗ Failed to update item: {response.status_code}")
    except Exception as e:
        print(f"✗ Error updating item: {e}")
    
    # Test getting specific item
    try:
        response = requests.get(f"{BASE_URL}/api/items/{item_id}/")
        if response.status_code == 200:
            print("✓ Specific item retrieved successfully")
        else:
            print(f"✗ Failed to get specific item: {response.status_code}")
    except Exception as e:
        print(f"✗ Error getting specific item: {e}")
    
    return True

def test_weather_api():
    """Test the Weather API"""
    print("\nTesting Weather API...")
    
    # Test getting weather data (should be empty initially)
    try:
        response = requests.get(f"{BASE_URL}/api/weather/")
        if response.status_code == 200:
            print("✓ Weather data retrieved successfully")
        else:
            print(f"✗ Failed to get weather data: {response.status_code}")
    except Exception as e:
        print(f"✗ Error getting weather data: {e}")
    
    # Test fetching weather data (this will fail without API key, but we can test the endpoint)
    try:
        weather_data = {"city": "London"}
        response = requests.post(f"{BASE_URL}/api/weather/fetch_weather/", json=weather_data)
        if response.status_code == 201:
            print("✓ Weather data fetched successfully")
        elif response.status_code == 400:
            print("⚠ Weather API key not configured (expected for test)")
        else:
            print(f"✗ Unexpected response: {response.status_code}")
    except Exception as e:
        print(f"✗ Error fetching weather data: {e}")

def test_dashboard():
    """Test the dashboard page"""
    print("\nTesting Dashboard...")
    
    try:
        response = requests.get(f"{BASE_URL}/dashboard/")
        if response.status_code == 200:
            print("✓ Dashboard loaded successfully")
        else:
            print(f"✗ Failed to load dashboard: {response.status_code}")
    except Exception as e:
        print(f"✗ Error loading dashboard: {e}")

def main():
    """Run all tests"""
    print("SBM API Test Suite")
    print("=" * 50)
    
    # Wait a moment for server to be ready
    print("Waiting for server to be ready...")
    time.sleep(2)
    
    # Test all endpoints
    test_items_api()
    test_weather_api()
    test_dashboard()
    
    print("\n" + "=" * 50)
    print("Test completed!")
    print("\nTo test the full application:")
    print("1. Open your browser and go to http://127.0.0.1:8000/dashboard/")
    print("2. Try creating items and fetching weather data")
    print("3. Check the interactive charts on the dashboard")

if __name__ == "__main__":
    main()
