# Use Cases for Enhanced Animal Collection System

### Use Case 01: Generate Structured Animal IDs

**As a user**
</br>**I want** animal IDs to follow a standardized format with meaningful components
</br>**So that** I can easily identify animals by their ID structure and creation year

### Use Case 02: Include Species Identifier in ID

**As a user**
</br>**I want** the animal's species reflected in its ID
</br>**So that** I can quickly identify the type of animal from its ID alone

### Use Case 03: Validate ID Format with Regex

**As a system**
</br>**I want** to enforce strict ID format validation
</br>**So that** only properly formatted IDs are accepted and data integrity is maintained

### Use Case 04: Test ID Generation with Timestamp

**As a developer**
</br>**I want** to verify that auto-generated IDs include the current year
</br>**So that** ID generation logic produces time-stamped identifiers correctly

### Use Case 05: Test Custom ID Assignment

**As a developer**
</br>**I want** to verify that manually provided IDs are validated and accepted
</br>**So that** the system can handle both auto-generated and pre-existing IDs

### Use Case 06: Implement Robust ID Validation

**As a system architect**
</br>**I want** invalid IDs to raise exceptions rather than silently fail
</br>**So that** data integrity issues are caught immediately and not propagated

### Use Case 07: Update Test Suite for New ID Format

**As a QA engineer**
</br>**I want** all existing tests updated to reflect the new ID structure
</br>**So that** the test suite validates current system behavior accurately

