DROP DATABASE IF EXISTS `jotvault_db`;

CREATE DATABASE `jotvault_db`;

DROP USER IF EXISTS 'jotvault_dev'@'localhost';
CREATE USER IF NOT EXISTS 'jotvault_dev'@'localhost' IDENTIFIED BY 'SecureP$ss123';
GRANT ALL PRIVILEGES ON `jotvault_db`.* TO 'jotvault_dev'@'localhost';
FLUSH PRIVILEGES;

USE `jotvault_db`;

CREATE TABLE `users` (
    `id` CHAR(36) PRIMARY KEY,
    `first_name` VARCHAR(35) NOT NULL,
    `last_name` VARCHAR(35) NOT NULL,
    `user_name` VARCHAR(64) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `pfp_url` VARCHAR(256),
    `password` VARBINARY(64) NOT NULL
);

INSERT INTO users (`id`, `first_name`, `last_name`, `user_name`, `email`, `password`)
    VALUES ("00000000-0000-0000-0000-000000000000", "admin", "admin", "admin", "admin@mail.com", 'admin');

CREATE TABLE `folders` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `parent_id` CHAR(36) DEFAULT '00000000-0000-0000-0000-000000000000',
    `user_id` CHAR(36) NOT NULL,

    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    CONSTRAINT `parent_folder_fk` FOREIGN KEY (`parent_id`) REFERENCES `folders` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

INSERT INTO folders (id, title, parent_id, user_id)
    VALUES ("00000000-0000-0000-0000-000000000000", "root", "00000000-0000-0000-0000-000000000000", "00000000-0000-0000-0000-000000000000");

CREATE TABLE `projects` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,

    `user_id` CHAR(36) NOT NULL,

    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `tasks` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `description` VARCHAR(2048) NOT NULL,
    `status` ENUM('todo', 'doing', 'done') DEFAULT 'todo',
    `color` CHAR(6) DEFAULT 'FFFFFF',
    `start` DATETIME DEFAULT CURRENT_TIMESTAMP,
    `end` DATETIME DEFAULT CURRENT_TIMESTAMP,

    `user_id` CHAR(36) NOT NULL,
    `project_id` CHAR(36),

    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `notes` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `content` TEXT NOT NULL,
    `status` ENUM('pinned', 'normal', 'archived', 'trashed') DEFAULT 'normal',
    `color` CHAR(6) DEFAULT 'FFFFFF',

    `user_id` CHAR(36) NOT NULL,
    `folder_id` CHAR(36) DEFAULT '00000000-0000-0000-0000-000000000000',
    `project_id` CHAR(36),

    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`folder_id`) REFERENCES `folders` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `notes_changelog` (
    `id` CHAR(36) PRIMARY KEY,
    `time_stamp` DATETIME NOT NULL,
    `offset` INT UNSIGNED NOT NULL,
    `modification` ENUM('addition', 'deletion') NOT NULL,
    `modified_data` VARCHAR(1024) NOT NULL,
    `note_id` CHAR(36) NOT NULL,

    FOREIGN KEY (`note_id`) REFERENCES `notes` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);
