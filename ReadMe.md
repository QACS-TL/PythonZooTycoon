# Use Cases for Enhanced Animal Collection System

### Use Case 01: Serialize Animals to JSON

**As a user**
</br>**I want** to save all animal data to a JSON file
</br>**So that** animal records persist between application sessions

### Use Case 02: Convert Animal Objects to Dictionaries

**As a system**
</br>**I want** each animal class to serialize its properties to a dictionary
</br>**So that** animal data can be saved in a structured format

### Use Case 03: Load Animals from JSON File

**As a user**
</br>**I want** the application to load existing animal data on startup
</br>**So that** I can continue working with previously saved animals

### Use Case 04: Reconstruct Animals from Dictionary Data

**As a system**
</br>**I want** to create appropriate animal instances from dictionary data
</br>**So that** saved animals are restored with correct class types and behaviors

### Use Case 05: Generate Sequential IDs from Existing Data

**As a system**
</br>**I want** new animal IDs to continue from the highest existing ID
</br>**So that** ID numbers remain unique and sequential across sessions


### Use Case 06: Implement Animal Factory Function

**As a developer**
</br>**I want** a centralized factory function to create animal instances
</br>**So that** object creation logic is consistent and maintainable

### Use Case 07: Calculate Expected ID Dynamically in Tests

**As a QA engineer**
**I want** tests to calculate expected IDs from actual file data
**So that** tests remain valid as animal data changes

### Use Case 08: Remove Hardcoded ID Values from Tests

**As a developer**
</br>**I want** tests to dynamically determine expected IDs
</br>**So that** tests don't break when existing animals are added or removed

### Use Case 09: Replace Hardcoded Animal Initialization

**As a developer**
</br>**I want** to load animals from file instead of hardcoding them
</br>**So that** the application uses persistent data as the source of truth

### Use Case 10: Implement Bidirectional Serialization

**As a developer**
</br>**I want** complete serialization and deserialization of animal objects
</br>**So that** data can round-trip between objects and JSON format without loss

### Use Case 11: Separate Factory Logic into Module

**As a developer**
</br>**I want** object creation logic in a dedicated factory module
</br>**So that** code follows separation of concerns principle