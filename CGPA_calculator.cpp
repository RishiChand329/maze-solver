#include <iostream>
#include <vector>
#include <iomanip>
using namespace std;

struct Subject {
    double gradePoint;
    int credit;
};

double calculateGPA(const vector<Subject>& subjects) {
    double totalPoints=0;
    int totalCredits=0;
    for(auto& s:subjects) {
        totalPoints+=s.gradePoint * s.credit;
        totalCredits+=s.credit;
    }
    return (totalCredits==0) ? 0 :totalPoints/totalCredits;
}

int main() {
    int semesters;
    cout<<"Enter number of semesters: ";
    cin>>semesters;

    double totalWeightedPoints=0;
    int totalCredits=0;

    for(int sem=1;sem<=semesters;++sem) {
        int subjectsCount;
        cout<<"\n--- Semester "<<sem<<" ---"<< endl;
        cout<<"Enter number of subjects: ";
        cin>>subjectsCount;

        vector<Subject> subjects(subjectsCount);
        for(int i = 0; i < subjectsCount; ++i) {
            cout<<"Subject "<<i+1<<" - Grade Point (out of 10): ";
            cin>>subjects[i].gradePoint;
            cout<<"Subject "<<i+1<<" - Credit: ";
            cin>>subjects[i].credit;
        }

        double gpa=calculateGPA(subjects);
        cout<<fixed<<setprecision(2);
        cout<<"> Semester "<<sem<<" GPA: "<<gpa<<endl;

        //Add to CGPA total
        for(auto& s:subjects) {
            totalWeightedPoints+=s.gradePoint*s.credit;
            totalCredits+=s.credit;
        }
    }

    double cgpa=(totalCredits==0) ? 0 :totalWeightedPoints/totalCredits;
    cout<<"\n Your CGPA after "<<semesters<<" semester(s) is: "<<fixed<<setprecision(2)<<cgpa<<endl;

    return 0;
}
