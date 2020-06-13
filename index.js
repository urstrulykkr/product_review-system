const express = require("express"),
	app = express(),
	path = __dirname + "/views/",
	bodyParser = require("body-parser"),
	morgan = require("morgan");

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
app.use((req, res) => {
	res.status(404).render("404");
});
