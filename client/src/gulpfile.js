'use strict';

var gulp = require('gulp');
var uglify = require('gulp-uglify');
var del = require('del');
var concat = require('gulp-concat');
var autoprefixer = require('gulp-autoprefixer');
var minifycss = require('gulp-minify-css');

var application_name = 'parlr-ui';

var sources = {
    images: 'images/**/*',
    pages: 'pages/**/*',
    scripts: [
        'bower_components/angular/angular.js',
        'bower_components/angular-route/angular-route.js',
        'bower_components/lodash/lodash.js',
        'bower_components/restangular/dist/restangular.js',
        'scripts/parlr-ui.js',
    ],
    styles: [
        'styles/*.scss',
    ]
};

var dist_path = '../dist';
var destination = {
    all: dist_path + '/**',
    images: dist_path + '/images',
    pages: dist_path + '/pages',
    scripts: dist_path + '/scripts',
    styles: dist_path + '/styles',
};

gulp.task('pages', function () {
    return gulp.src(sources.pages)
        .pipe(gulp.dest(destination.pages));
});

gulp.task('images', function () {
    return gulp.src(sources.images)
        .pipe(gulp.dest(destination.images));
});

gulp.task('scripts', function () {
    return gulp.src(sources.scripts)
        .pipe(uglify())
        .pipe(concat(application_name + '.min.js'))
        .pipe(gulp.dest(destination.scripts));
});

gulp.task('styles', function () {
    return gulp.src(sources.styles)
        .pipe(concat(application_name + '.min.css'))
        .pipe(autoprefixer('last 3 version'))
        .pipe(minifycss())
        .pipe(gulp.dest(destination.styles));
});

gulp.task('clean', function (callback) {
    del(destination.all, {force: true}, callback);
});

gulp.task('build', ['clean'], function () {
    gulp.start('scripts', 'styles', 'images', 'pages');
});

gulp.task('watch', ['build'], function () {
    gulp.watch(sources.styles, ['styles']);
    gulp.watch(sources.scripts, ['scripts']);
    gulp.watch(sources.images, ['images']);
    gulp.watch(sources.pages, ['pages']);
});


gulp.task('default', ['build'], function () {

});