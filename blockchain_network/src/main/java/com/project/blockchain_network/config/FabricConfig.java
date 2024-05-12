package com.project.blockchain_network.config;

import org.hyperledger.fabric.sdk.*;
import org.hyperledger.fabric.gateway.Gateway;
import org.hyperledger.fabric.gateway.Network;
import org.hyperledger.fabric.gateway.Wallet;
import org.hyperledger.fabric.gateway.Wallets;
import org.springframework.beans.factory.annotation.Value;
import org.springframework.context.annotation.Bean;
import org.springframework.context.annotation.Configuration;

import java.io.IOException;
import java.nio.file.Path;
import java.nio.file.Paths;

@Configuration
public class FabricConfig {

    @Value("${fabric.gateway.wallet}")
    private String walletPath;

    @Value("${fabric.gateway.network}")
    private String networkConfigPath;

    @Bean
    public Gateway gateway() throws IOException {
        // Load wallet
        Path walletDirectory = Paths.get(walletPath);
        Wallet wallet = Wallets.newFileSystemWallet(walletDirectory);

        // Load network configuration
        Path networkConfigFile = Paths.get(networkConfigPath);

        // Create gateway connection
        Gateway.Builder builder = Gateway.createBuilder()
                .identity(wallet, "user1")
                .networkConfig(networkConfigFile);

        return builder.connect();
    }

    @Bean
    public Network network(Gateway gateway) {
        // Connect to the network
        return gateway.getNetwork("mychannel");
    }

    @Bean
    public Contract contract(Network network) {
        // Get contract from the network
        return network.getContract("mychaincode");
    }
}
