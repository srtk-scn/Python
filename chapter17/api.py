

# import requests

# x = requests.get('https://w3schools.com/python/demopage.htm')

# print(x.text)
package com.palamida.datamodel.dao.impl;

import org.apache.commons.lang.RandomStringUtils;
import java.sql.*;

public class GlobalInv {
    public static void main(String[] args) {
        try {
            String dbURL = "jdbc:mysql://localhost:3306/codeinsightr4?user=root&password=password";
            Class.forName("com.mysql.cj.jdbc.Driver");
            java.sql.Connection con = DriverManager.getConnection(dbURL);
            Statement stmt = con.createStatement();
            System.out.println("Connection established..!!");
            PreparedStatement insert = con.prepareStatement("INSERT INTO pas_inventory_flex_fields (INVENTORY_ID_, FLEX_FIELD_1_, FLEX_FIELD_2_, FLEX_FIELD_3_, FLEX_FIELD_4_, FLEX_FIELD_5_" +
                    ") VALUES (?,?,?,?,?,?) ");

            String select = "select ID_ from codeinsightr4.PSE_INVENTORY_GROUPS";
            ResultSet invrs = stmt.executeQuery(select);

            Statement stmt2 = con.createStatement();
            String select2 = "select TEXT_ from codeinsightr4.pdl_license";
            ResultSet licrs = stmt2.executeQuery(select2);

            int size = 0;
            while (invrs.next()) {
                if (!licrs.next()) {
                    Statement stmt3 = con.createStatement();
                    licrs = stmt3.executeQuery(select2);
                    licrs.next();
                }
                size++;
                if(size == 100) {
                    break;
                }
                System.out.println("Inventory Id " + invrs.getInt("ID_"));
//                System.out.println("License Text: " + licrs.getString("TEXT_"));
                insert.setInt(1, invrs.getInt("ID_"));//1 specifies the first parameter in the query
                String textToInsert = getActualText(size, licrs.getString("TEXT_"));

                insert.setString(2, textToInsert);
                insert.setString(3, textToInsert);
                insert.setString(4, textToInsert);
                insert.setString(5, textToInsert);
                insert.setString(6, textToInsert);
                insert.executeUpdate();
//                System.out.println("Text: " + textToInsert);
            }
            System.out.println("Inventory count " + size);


        } catch (ClassNotFoundException c) {
            c.printStackTrace();
        } catch (SQLException e) {
            System.out.println("Error while executing the query.. updating the codebase path");
            e.printStackTrace();
        }

    }

    private static String generateRandomData() {
        return RandomStringUtils.randomAlphanumeric(30);
    }

    private static String getActualText(int size, String licString) {
//        return generateRandomData();
        switch (size % 10) {
            case 1:
            case 4:
            case 8:
                return licString;
            case 2:
            case 3:
            case 5:
            case 7:
            case 9:
            case 10:
                return generateRandomData();
            case 0:
            case 6:
                return String.valueOf(Math.random());
            default:
                return licString;
        }
    }
}



import requests

host = "http://localhost:8888/codeinsight/api"
preferences = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6MSwiaWF0IjoxNjI3OTc5OTczfQ.q1GPE5PPEBHKpBwR2yOht1VGL-i4yrRXJx11MNID3P5GWrpsZAiTnAscsWHfiJIbb9EBmdjFICw8zNaYo8S7_w"
session = requests.Session()
session.headers.update({'Authorization': preferences})

for each in range(0,2000000):
    req = {
        "projectId": "1525",
        "inventoryModel": {
            "name": "Inventory-" + str(each),
            "inventoryType": "COMPONENT",
            "component": {
                "id": "58316",
                "versionId": "3704669",
                "licenseId": "158"
            },
            "licenseId": "158"

        }
    }
    response = session.post("{}/inventories".format(host), json=req)
    # print(response)
    if each%1000==0:
        print(each)




# host = "http://localhost:8888/codeinsight/api"preferences = "Bearer eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiJhZG1pbiIsInVzZXJJZCI6MSwiaWF0IjoxNjM1NDc0NTE4fQ.g-kTBB_Ml2fyMWLdnDd0lEsKxSPRgTfh3typu8PIL6S-YNbkRFVL3VTaUxI1jG9NkixqG30J-f12LpAQgCdw4w"
# session = requests.Session()
# session.headers.update({'Authorization': preferences})

# for each in range(0,5):
#     req = {
#         "projectId": "3",
#         "inventoryModel": {
#             "name": "Inventory-" + str(each),
#             "inventoryType": "COMPONENT",
#             "component": {
#                 "id": "58316",
#                 "versionId": "3704669",
#                 "licenseId": "158"
#             },
#             "licenseId": "158"
#         }
#     }
#     response = session.post("{}/inventories".format(host), json=req)
#     print(response)

