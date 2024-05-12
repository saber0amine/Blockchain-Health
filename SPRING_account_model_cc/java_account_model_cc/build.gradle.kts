import org.gradle.api.JavaVersion
import com.github.jengelman.gradle.plugins.shadow.tasks.ShadowJar

plugins {
    id("com.github.johnrengelman.shadow") version "7.0.0"
    id("java")
}

group = "org.hyperledger.fabric-chaincode-java"
version = "1.0-SNAPSHOT"

java.sourceCompatibility = JavaVersion.VERSION_1_8

repositories {
    mavenLocal()
    mavenCentral()
    maven {
        url = uri("https://jitpack.io")
    }
}

dependencies {
    implementation("org.hyperledger.fabric-chaincode-java:fabric-chaincode-shim:2.3.0")
    implementation("com.fasterxml.jackson.core:jackson-databind:2.9.10")
    implementation("com.github.everit-org.json-schema:org.everit.json.schema:1.12.1")
    testImplementation("junit:junit:4.12")
}

tasks.named<ShadowJar>("shadowJar") {
    configurations = project.configurations.filter { it.name == "implementation" }
    manifest {
        attributes["Main-Class"] = "org.hyperledger.fabric.chaincode.MedicalRecordChaincode"
    }
}
