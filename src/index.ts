import express from "express";
const app = express();
import bodyParser from "body-parser";
import { URLSearchParams } from "url";
import path from "path";
import fs from "fs";
import axios from "axios";
const { name, version } = require("../package.json");
import { config } from "dotenv";
config();

app.use(bodyParser.urlencoded({ extended: true }));
app.use(bodyParser.json({ limit: "50mb" }));
app.set("trust proxy", 1);


app.get("/", async (req, res) => {
    return res.status(200).json({
        name,
        version,
        message: `Welcome to ${name} v${version}`,
    });
});




app.get("*", async (req, res) => {
    return res.status(404).json({
        error: "404",
        message: "Page not found",
        route: req.path,
        query: req.query,
        params: req.params,
    });
});

app.listen(process.env.PORT || 80, () => {
    console.clear();
    console.log(
        `${name.replaceAll("-", " ")} v${version} is listening at http://localhost:${process.env.PORT || 80}`
    );
});
