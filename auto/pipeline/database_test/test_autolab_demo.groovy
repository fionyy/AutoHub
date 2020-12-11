//测试路径
test_plan = "./auto/plan/database_test/test_autolab_demo.py"

node{
    stage("Init"){
        echo "Init run env"

    }

    stage("CheckOUT"){
        echo "check out last code"
        checkout scm

    }

    stage("Test"){

        powershell "pytest --version"
        dir("."){
            powershell "pwd"
            powershell "pytest ${test_plan} --html=./logs/report.html  --self-contained-html"
        }

    }

    stage("Report"){
        dir("."){
            publishHTML (target: [
                allowMissing: false,
                alwaysLinkToLastBuild: false,
                keepAll: True,
                reportDir: "logs",
                reportFiles: "report.html",
                reportName: "HTML report"

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