const express = require("express");
const path = require("path");
const { newTask } = require("./gameHandler");

const app = express();
const PORT = 3000;

const projectDirectory = path.join(__dirname, "..", "..");

app.use(express.urlencoded({ extended: true }));

app.use(express.static(path.join(__dirname, "..", "/css")));
app.use(express.static(path.join(__dirname, "..", "/res")));

app.get("/", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/mainPage.html");
});

app.get("/mainPage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/mainPage.html");
});

app.get("/createFilePage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/createFilePage.html");
});

app.get("/finiteGameModePage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/finiteGameModePage.html");
});

app.get("/finiteGamePage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/finiteGamePage.html");
});

app.get("/resultPage", (req, res) => {
  res.sendFile(projectDirectory + "/src/html/resultPage.html");
});

app.post("/create_file", require("./createFileHandler").generateFile);

app.post("/start_game", require("./gameHandler").redirectFiniteGame);

app.post("/new_task", (req, res) => {
  res.send(newTask(Number(req.body.size), "Addition"));
});

app.get("/result", (req, res) => {
  res.redirect(
    "/resultPage" + "?num=" + req.body.num + "&result=" + req.body.result
  );
});

app.post("/download", require("./createFileHandler").downloadFile);

app.listen(PORT, () => {
  console.log(`Сервер запущен на порту ${PORT}`);
});
