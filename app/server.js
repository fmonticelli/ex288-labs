const express = require("express");
const fs = require("fs");

const app = express();

const port = process.env.PORT || 8080;
const message = process.env.APP_MESSAGE || "EX288 lab funcionando!";

app.get("/", (req, res) => {
  res.send(message + "\n");
});

app.get("/health", (req, res) => {
  res.status(200).json({
    status: "ok"
  });
});

app.get("/write", (req, res) => {
  fs.writeFileSync("/opt/app-root/src/data/teste.txt", message + "\n");
  res.send("Arquivo gravado\n");
});

app.listen(port, "0.0.0.0", () => {
  console.log(`Aplicacao escutando na porta ${port}`);
});