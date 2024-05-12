package com.project.blockchain_network.config;

import org.hyperledger.fabric.sdk.NetworkConfig;
import org.hyperledger.fabric.sdk.Orderer;
import org.hyperledger.fabric.sdk.exception.InvalidArgumentException;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.IOException;

@Configuration
public class FabricNetworkConfig {

    @Bean
    public NetworkConfig getNetworkConfig() throws InvalidArgumentException, IOException {
        // Define network configuration
        NetworkConfig.Builder networkConfigBuilder = NetworkConfig.newBuilder();

        // Define orderer
        Orderer orderer = Orderer.newBuilder()
                .name("orderer.example.com")
                .url("grpc://localhost:7050")
                .build();

        // Define peer organizations
        PeerOrg hospital1 = PeerOrg.newBuilder()
                .name("Hospital1")
                .mspid("Hospital1MSP")
                .peerUrl("grpc://localhost:7051")
                .caLocation("http://localhost:7054")
                .ordererLocation("grpc://localhost:7050")
                .build();

        PeerOrg hospital2 = PeerOrg.newBuilder()
                .name("Hospital2")
                .mspid("Hospital2MSP")
                .peerUrl("grpc://localhost:8051")
                .caLocation("http://localhost:8054")
                .ordererLocation("grpc://localhost:7050")
                .build();

        PeerOrg hospital3 = PeerOrg.newBuilder()
                .name("Hospital3")
                .mspid("Hospital3MSP")
                .peerUrl("grpc://localhost:9051")
                .caLocation("http://localhost:9054")
                .ordererLocation("grpc://localhost:7050")
                .build();

        // Add organizations to network configuration
        networkConfigBuilder.orderers(orderer)
                .addPeerOrgs(hospital1, hospital2, hospital3);

        return networkConfigBuilder.build();
    }
}
