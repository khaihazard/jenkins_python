podTemplate(containers: [
  containerTemplate(
    name: 'python', 
    image: 'jenkins/inbound-agent-python:latest', 
    command: 'sleep', 
    args: '30d')
]) 
{
  node(POD_LABEL)
  {
    stage('Get a Python Project')
    {
      container('python')
      {
          stage('Checkout Code')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'apt install nano'
            sh 'apt install pip'
            echo 'Y'
            sh 'apt install python3'
            sh 'python3 -V'
            sh 'hostname'
            sh 'git clone https://github.com/khaihazard/jenkins_python.git'
            sh 'ls -la jenkins_python'
            sh 'python3 jenkins_python/cal.py'
          }
          stage(' Installing packages')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'apt install -y pip'
            sh 'pip install requests'
            sh 'python3 jenkins_python/cal.py'
          }
          stage('Static Code Check')
          {
            sh 'pwd'
            sh 'ls -la'
            sh 'python3 -V'
            sh 'ls -la jenkins_python'
            sh 'python3 jenkins_python/cal.py'
          }
          stage('Unit Test Check')
          {
            sh 'python jenkins_python/socket.py'          
          }
        
      }
    }
  }
}
