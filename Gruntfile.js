module.exports = function (grunt) {
    'use strict';

    grunt.initConfig({
        pkg: grunt.file.readJSON('package.json'),

        compass: {
            robtheme: {
                options: {
                    sassDir: 'scss/',
                    cssDir: 'stylesheets/',
                },
            },
            sharedRobtheme: {
                options: {
                    sassDir: 'scss/Dropbox/sharedRobtheme',
                    cssDir: 'stylesheets/',
                }
            }
        },
        concat: {
            options: {
                separator: '',
            },
            robtheme: {
                src: ['stylesheets/robtheme.css',
                      'stylesheets/sharedRobtheme.css'],
                dest: 'stylesheets/robtheme-concat.css',
            }
        },
        cssmin: {
            target : {
                src : ["stylesheets/robtheme-concat.css"],
                dest : "stylesheets/robtheme.min.css",
            }
        },
        watch: {
            ulearn: {
                files: [
                    'scss/*.scss',
                    'scss/Dropbox/sharedRobtheme/*.scss'
                ],
                tasks: ['compass:robtheme', 'compass:sharedRobtheme', 'concat:robtheme', 'cssmin']
            }
        },
        browserSync: {
            plone: {
                bsFiles: {
                    src : [
                      'stylesheets/*.css'
                    ]
                },
                options: {
                    watchTask: true,
                    debugInfo: true,
                    proxy: "localhost:8080/Plone",
                    reloadDelay: 3000,
                    // reloadDebounce: 2000,
                    online: true
                }
            }
        }
    });

    // grunt.loadTasks('tasks');
    grunt.loadNpmTasks('grunt-browser-sync');
    grunt.loadNpmTasks('grunt-contrib-watch');
    grunt.loadNpmTasks('grunt-contrib-compass');
    grunt.loadNpmTasks('grunt-contrib-concat');
    grunt.loadNpmTasks('grunt-contrib-cssmin');

    // CWD to theme folder
    grunt.file.setBase('./genweb/robtheme');

    // Registered tasks: grunt watch
    grunt.registerTask('default', ["browserSync:plone", "watch"]);
    grunt.registerTask('bsync', ["browserSync:html", "watch"]);
    grunt.registerTask('plone-bsync', ["browserSync:plone", "watch"]);
    grunt.registerTask('minify', ['uglify']);
};
