const express = require("express");

const app = express();

const port = process.env.PORT || 8080;
const message = process.env.APP_MESSAGE || "Hello from EX288";

app.get("/", (req, res) => {
  res.send(message + "\n");
});

app.get("/health", (req, res) => {
  res.status(200).json({ status: "ok" });
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Listening on port ${port}`);
});