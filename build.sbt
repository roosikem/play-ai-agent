name := "play-ai-agent"

version := "1.0"

lazy val root = (project in file(".")).enablePlugins(PlayJava)

scalaVersion := "2.13.8"

libraryDependencies ++= Seq(
  guice,
  javaJdbc,
  javaWs,
  "org.scalatestplus.play" %% "scalatestplus-play" % "5.1.0" % Test
)