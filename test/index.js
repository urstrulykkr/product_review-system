const chai = require("chai"),
	chaiHttp = require("chai-http"),
	server = "localhost:5000",
	should = chai.should(),
	expect = chai.expect;
chai.use(chaiHttp);
describe("GET /", () => {
	it("should load homepage", (done) => {
		chai.request(server)
			.get("/")
			.end((err, res) => {
				if (err) console.log(err);
				res.should.have.status(200);
				res.should.have.property("type").equal("text/html");
				res.should.have.property("text");
				done();
			});
	});
});
describe("POST /getRating", () => {
	it("should send back rating", (done) => {
		chai.request(server)
			.post("/getRating")
			.send({input: "Hello World!"})
			.end((err, res) => {
				if (err) console.log(err);
				res.should.have.status(200);
				res.should.have.property("type").equal("application/json");
				res.should.have.property("body");
				res.body.should.be.a("string");
				expect(res.body.trim()).to.match(/^(\d+(?:\.\d+)?) (\bstar\b)$/);
				done();
			});
	}).timeout(3000);
});
