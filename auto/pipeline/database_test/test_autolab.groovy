def testplan = "./auto/plan/database_test/test_autolab.py"

node {
    stage("Init"){
        echo "Init Run Env"
    }

    stage("Check out"){
        echo "check out last code"
        checkout scm

    }

    stage("Test"){
        powershell.exe --command "pytest --version"
        dir("."){
            powershell "pwd"
            powershell "pytest ${testplan} --html=./logs/report.html --self-contained-html"
        }
    }

    stage("Report"){
        dir("."){
            publishHTML (target:[
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: true,
                reportDir: 'logs',
                reportFiles: 'report.html',
                reportName: "HTML Report"
            ])
        }
    }

    stage("Notify"){
        script{
            if ( currentBuild.currentResult == "SUCCESS"){
                echo "it is build success"
            }
            else{
                echo "it is build failed"
            }
        }
    }
}