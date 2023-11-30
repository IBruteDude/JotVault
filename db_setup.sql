DROP DATABASE IF EXISTS `jotvault_db`;

CREATE DATABASE `jotvault_db`;

CREATE USER IF NOT EXISTS 'jotvault_dev'@'localhost' IDENTIFIED BY 'SecureP@ss123';
GRANT ALL PRIVILEGES ON `jotvault_db`.* TO 'hbnb_dev'@'localhost';
FLUSH PRIVILEGES;

USE `jotvault_db`;

CREATE TABLE `folders` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `parent_id` CHAR(36),

    CONSTRAINT `parent_folder_fk` FOREIGN KEY (`parent_id`) REFERENCES `folders` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `users` (
    `id` CHAR(36) PRIMARY KEY,
    `first_name` VARCHAR(35) NOT NULL,
    `last_name` VARCHAR(35) NOT NULL,
    `user_name` VARCHAR(64) NOT NULL,
    `email` VARCHAR(256) NOT NULL,
    `pfp_url` VARCHAR(75) NOT NULL,

    `password` VARBINARY(64) NOT NULL
);

CREATE TABLE `tasks` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `description` VARCHAR(2048) NOT NULL,
    `status` ENUM('todo', 'doing', 'done') DEFAULT 'todo',
    `user_id` CHAR(36) NOT NULL,

    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `notes` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL,
    `content_url` VARCHAR(75) NOT NULL,
    `status` ENUM('pinned', 'normal', 'archived', 'trashed') DEFAULT 'normal',
    `user_id` CHAR(36) NOT NULL,
    `folder_id` CHAR(36) NOT NULL,

    FOREIGN KEY (`user_id`) REFERENCES `users` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`folder_id`) REFERENCES `folders` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
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

CREATE TABLE `projects` (
    `id` CHAR(36) PRIMARY KEY,
    `title` VARCHAR(256) NOT NULL
);

CREATE TABLE `project_notes_assoc` (
    `project_id` CHAR(36),
    `note_id` CHAR(36),

    PRIMARY KEY (`project_id`, `note_id`),
    UNIQUE KEY (`note_id`),

    FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`note_id`) REFERENCES `notes` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `project_tasks_assoc` (
    `project_id` CHAR(36),
    `task_id` CHAR(36),

    PRIMARY KEY (`project_id`, `task_id`),
    UNIQUE KEY (`task_id`),

    FOREIGN KEY (`project_id`) REFERENCES `projects` (`id`) ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE `task_timestamps` (
    `task_id` CHAR(36) PRIMARY KEY,
    `start` DATETIME NOT NULL,
    `end` DATETIME NOT NULL,

    FOREIGN KEY (`task_id`) REFERENCES `tasks` (`id`) ON UPDATE CASCADE ON DELETE CASCADE
);
