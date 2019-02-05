DROP TABLE IF EXISTS tests;
DROP TABLE IF EXISTS exams;
CREATE TABLE tests (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	format TEXT NOT NULL,
	exam INTEGER NOT NULL,
	start INTEGER NOT NULL,
	finish INTEGER NOT NULL CHECK(finish > start),
	marked INTEGER NOT NULL CHECK(marked=0 OR marked=1 OR marked=2), -- 0:unmarked 1:marked 2:feedback_given
	result INTEGER NOT NULL CHECK(result>=0 AND result<=100),
	FOREIGN KEY (exam) REFERENCES exams(id)
);
CREATE TABLE exams (
	id INTEGER PRIMARY KEY AUTOINCREMENT,
	created INTEGER NOT NULL, --UNIX timestamp for time exam created
	creator INTEGER NOT NULL, -- userid of employer / admin who created exam
	details TEXT NOT NULL, -- solution filename
	timer INTEGER NOT NULL DEFAULT 300 CHECK(timer>0),
	difficulty INTEGER NOT NULL CHECK(difficulty>=0 AND difficulty<=10)
);
