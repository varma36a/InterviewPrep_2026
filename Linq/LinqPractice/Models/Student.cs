namespace LinqPractice.Models;

public record Student(
    int Id,
    string Name,
    int Age,
    string Major,
    double Gpa);

public record Course(
    int Id,
    string Title,
    string Department,
    int Credits);

public record Enrollment(
    int StudentId,
    int CourseId,
    int? Grade);
