package org.hyperledger.fabric.chaincode;

// Import necessary libraries
import java.util.List;
import org.hyperledger.fabric.contract.Context;
import org.hyperledger.fabric.contract.ContractInterface;
import org.hyperledger.fabric.contract.annotation.Contract;
import org.hyperledger.fabric.contract.annotation.Default;
import org.hyperledger.fabric.contract.annotation.Info;
import org.hyperledger.fabric.contract.annotation.Transaction;
import org.hyperledger.fabric.shim.ChaincodeException;
import org.hyperledger.fabric.shim.ChaincodeStub;

import com.fasterxml.jackson.databind.ObjectMapper;

// Define the contract
@Contract(
        name = "MedicalRecordChaincode",
        info = @Info(
                title = "Medical Record Chaincode",
                description = "Smart contract for managing medical records",
                version = "1.0"
        )
)
@Default
public class MedicalRecordChaincode implements ContractInterface {

    // Prefix for medical record keys
    private static final String RECORD_PREFIX = "MEDICAL_RECORD_";

    // Inner class representing a medical record
    private class MedicalRecord {
        private String patientId;
        private String organizationId;
        private String data;

        // Constructor
        public MedicalRecord(String patientId, String organizationId, String data) {
            this.patientId = patientId;
            this.organizationId = organizationId;
            this.data = data;
        }

        // Getter methods
        public String getPatientId() {
            return patientId;
        }

        public String getOrganizationId() {
            return organizationId;
        }

        public String getData() {
            return data;
        }
    }

    // Method to create a medical record
    @Transaction
    public void createMedicalRecord(Context ctx, String patientId, String organizationId, String data) {
        // Validate input arguments
        if (!isValidString(patientId) || !isValidString(organizationId) || !isValidString(data)) {
            throw new ChaincodeException("Invalid arguments");
        }

        // Construct the record key
        String recordKey = RECORD_PREFIX + patientId + "_" + organizationId;

        // Check if the record already exists
        if (recordExists(ctx, recordKey)) {
            throw new ChaincodeException("Medical record already exists");
        }

        // Create a new medical record instance
        MedicalRecord record = new MedicalRecord(patientId, organizationId, data);

        try {
            // Store the record in the ledger
            ctx.getStub().putState(recordKey, new ObjectMapper().writeValueAsBytes(record));
        } catch (Exception e) {
            throw new ChaincodeException("Error creating medical record: " + e.getMessage());
        }
    }

    // Method to get a medical record
    @Transaction
    public String getMedicalRecord(Context ctx, String patientId, String organizationId) {
        // Validate input arguments
        if (!isValidString(patientId) || !isValidString(organizationId)) {
            throw new ChaincodeException("Invalid arguments");
        }

        // Construct the record key
        String recordKey = RECORD_PREFIX + patientId + "_" + organizationId;

        // Retrieve the record from the ledger
        byte[] recordBytes = ctx.getStub().getState(recordKey);

        // Check if the record exists
        if (recordBytes == null || recordBytes.length == 0) {
            throw new ChaincodeException("Medical record not found");
        }

        // Return the record data
        return new String(recordBytes);
    }

    // Utility method to check if a string is valid
    private boolean isValidString(String str) {
        return str != null && !str.trim().isEmpty();
    }

    // Utility method to check if a record exists
    private boolean recordExists(Context ctx, String recordKey) {
        byte[] recordBytes = ctx.getStub().getState(recordKey);
        return (recordBytes != null && recordBytes.length > 0);
    }
}
