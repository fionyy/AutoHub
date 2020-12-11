def test_plan = "./auto/plan/database_test/test_crm_resume.py"

node{
    stage("Init"){
        echo "init env"
    }

    stage("Checkout"){
        echo "check out last code"
        checkout scm

    }


    stage("Test"){
        powershell "pytest --version"
        dir("."){
            powershell "pwd"
            powershell "pytest ${test_plan} --html=./logs/report.html --self-contained-html"
        }

    }

    stage("Report"){
        dir("."){
            publishHTML(target:[
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                killAll: true,
                reportDir: "logs",
                reportFiles: "report.html",
                reportName: "HTML Report"

            ])
        }
    }

    stage("Notify"){
        script{
            if (currentBuild.currentResult == "SUCCESS"){
                echo "it is build success"
            }else{
                echo "it is build failed"
            }
        }
    }
}