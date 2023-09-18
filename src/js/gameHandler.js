const { generateSingleTask } = require("./tasks");

const redirectFiniteGame = (req, res) => {
  res.redirect("/finiteGamePage" + "?size=" + req.body.size + "&num=" + req.body.num);
};

function newTask(size) {
  return generateSingleTask(size, "Addition");
}

module.exports = {
  redirectFiniteGame,
  newTask,
};
