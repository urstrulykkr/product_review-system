const express = require("express"),
	app = express(),
	path = __dirname + "/views/",
	bodyParser = require("body-parser"),
	morgan = require("morgan"),
	{ spawn } = require("child_process");

app.use(morgan("dev"));
app.use(bodyParser.json());
app.use(
	bodyParser.urlencoded({
		extended: false,
	})
);
app.set("port", 5000);
app.use(express.static(__dirname + "/public"));
app.set("views", path);
app.set("view engine", "ejs");
app.listen(app.get("port"), () => {
	console.log("App is running on port", app.get("port"));
});

app.get("/", (req, res) => {
	res.render("index");
});
app.post("/getRating", (req, res) => {
	var pythonOutput;
	const python = spawn("python", ["getRating.py", req.body.input]);
	python.stdout.on("data", (data) => {
		pythonOutput = data.toString();
	});
	python.on("close", (code) => {
		console.log(`Python exit code: ${code}`);
		console.log(pythonOutput);
		res.json(pythonOutput);
	});
});
app.use((req, res) => {
	res.status(404).render("404");
});
