package org.hyperledger.fabric.chaincode.Models;

// Define the class representing a medical record
public class MedicalRecord {
    // Attributes
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
