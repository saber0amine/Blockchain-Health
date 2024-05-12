package com.project.blockchain_network.cryptoMateriels;
import java.nio.file.Path;
import java.nio.file.Paths;
import org.hyperledger.fabric_ca.sdk.EnrollmentRequest;
import org.hyperledger.fabric_ca.sdk.HFCAClient;
import org.hyperledger.fabric_ca.sdk.RegistrationRequest;
import org.hyperledger.fabric_ca.sdk.exception.EnrollmentException;
import org.hyperledger.fabric_ca.sdk.exception.InfoException;
import org.hyperledger.fabric_ca.sdk.exception.RegistrationException;

public class CryptoMaterialGenerator {

    // CA server connection parameters
    private static final String CA_URL = "http://localhost:7054";
    private static final String CA_ADMIN_USERNAME = "admin";
    private static final String CA_ADMIN_PASSWORD = "adminpw";
    private static final String CA_CHAINCODE_ORG = "org1";

    // Path to the wallet directory
    private static final Path WALLET_PATH = Paths.get("/path/to/wallet");

    public static void main(String[] args) throws Exception {
        // Create HFCAClient instance
        HFCAClient caClient = HFCAClient.createNewInstance(CA_URL, null);

        // Enroll admin user
        enrollAdmin(caClient);

        // Register and enroll new user
        registerAndEnrollUser(caClient, "user1", "org1.department1");
    }

    // Enroll admin user
    private static void enrollAdmin(HFCAClient caClient) throws EnrollmentException, InfoException {
        EnrollmentRequest enrollmentRequest = new EnrollmentRequest();
        enrollmentRequest.addHost("localhost");

        // Enroll admin user
        caClient.enroll(CA_ADMIN_USERNAME, CA_ADMIN_PASSWORD, enrollmentRequest);
    }

    // Register and enroll new user
    private static void registerAndEnrollUser(HFCAClient caClient, String username, String affiliation) throws RegistrationException, EnrollmentException {
        // Create registration request
        RegistrationRequest registrationRequest = new RegistrationRequest(username, affiliation);

        // Register new user
        String enrollmentSecret = caClient.register(registrationRequest, caClient.getAdmin());

        // Enroll new user
        caClient.enroll(username, enrollmentSecret);
    }
}
