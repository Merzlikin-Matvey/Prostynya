const { generateSingleTask } = require('./tasks');

const redirect = (req, res) => {
    res.redirect('/gamePage' + '?size=' + req.body.size + '&num=' + req.body.num);
}

function newTask(size){
    return (generateSingleTask(size, "Addition"))
}

module.exports = {
    redirect,
    newTask
}



