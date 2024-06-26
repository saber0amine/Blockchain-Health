# Blockchain-Based Healthcare Application (BCA)

## Overview

The Blockchain-Based Healthcare Application (BCA) is a decentralized healthcare platform built on Hyperledger Fabric, designed to address the challenges of managing patient medical records in Morocco's healthcare ecosystem. The application aims to streamline data sharing, enhance interoperability, and improve access to comprehensive patient histories for healthcare providers, while empowering patients with greater control over their medical information.

## Features

- Decentralized platform for storing and managing patient medical records
- Secure data sharing between healthcare providers via Hyperledger Fabric channels
- Patient-controlled access and consent management for sharing medical information
- Integration with traditional medicine practices for personalized healthcare guidance
- AI-powered recommendation systems for healthcare services based on patient medical history

## Technical Specifications

- **Blockchain Framework:** Hyperledger Fabric
- **Database:** CouchDB
- **Smart Contracts:** Chaincode written in Go
- **API:** RESTful APIs for interaction with the Fabric network
- **User Interface:** mobile-based interface for healthcare providers and patients
- **Identity Management:** Hyperledger Fabric Membership Service Provider (MSP)
- **Encryption:** Data encryption using cryptographic techniques (hashing, encryption)

## Installation and Setup

### Prerequisites

- Docker
- Node.js
- Go / java programming language

### Installation Steps

1. Clone the repository:
   ```
   git clone https://github.com/your-repo/bca.git
   ```

2. Navigate to the project directory:
   ```
   cd blockcì_network
   ```

3. Install dependencies:
   ```
   npm install
   ```

4. Start the Hyperledger Fabric network:
   ```
   ./start.sh
   ```

5. Deploy the smart contracts:
   ```
   ./deploy.sh
   ```

6. Start the API server:
   ```
   npm start
   ```

## Usage

1. Access the mobile interface for healthcare providers at [http://localhost:3000/provider](http://localhost:3000/provider).
2. Access the mobileinterface for patients at [http://localhost:3000/patient](http://localhost:3000/patient).
3. Follow the on-screen instructions to register, log in, and access the application features.

## Contribution
AMINE SABER 
HOUSSAM CHAHIDI 
EZZAHNOUNI YOUSSEF

Contributions to the Blockchain-Based Healthcare Application (BCA) project are welcome! If you encounter any issues or have suggestions for improvements, please feel free to open an issue or submit a pull request on GitHub.

## License

This project is licensed under the [MIT License](LICENSE).

---

Feel free to customize this README file according to your project's specific requirements and features.