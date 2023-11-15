DROP TABLE IF EXISTS file_lines;
DROP TABLE IF EXISTS source_files;
DROP TABLE IF EXISTS projects;

CREATE TABLE projects (
    project_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    project_name TEXT NOT NULL,
    project_path TEXT NOT NULL
);

CREATE TABLE source_files (
    file_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    project_id INTEGER,
    file_path TEXT NOT NULL,
    file_name TEXT NOT NULL,
    file_lang TEXT,
    FOREIGN KEY (project_id) REFERENCES projects (project_id)
);

CREATE TABLE file_lines (
    line_id INTEGER PRIMARY KEY AUTO_INCREMENT,
    file_id INTEGER,
    line_number INTEGER NOT NULL,
    line_text TEXT NOT NULL,
    FOREIGN KEY (file_id) REFERENCES source_files (file_id)
);