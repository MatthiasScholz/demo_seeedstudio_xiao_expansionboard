{
  pkgs,
  lib,
  config,
  inputs,
  ...
}:

{
  # https://devenv.sh/basics/
  env.GREET = "camper smart switch";

  # https://devenv.sh/packages/
  packages = [
    # Manage dependencies
    pkgs.circup
    # IDE
    pkgs.thonny
    # flash
    pkgs.esptool
    # REPL
    pkgs.picocom
  ];

  # https://devenv.sh/languages/
  # languages.rust.enable = true;

  # https://devenv.sh/processes/
  # processes.dev.exec = "${lib.getExe pkgs.watchexec} -n -- ls -la";

  # Sync local changes to the device to avoid losing content
  # when developing on the device directly
  # NOTE Works for MacOSX
  # TODO avoid repetition
  processes.sync.exec = "rsync -avz --del code.py /Volumes/CIRCUITPY/code.py";
  script.sync.exec = "rsync -avz --del code.py /Volumes/CIRCUITPY/code.py";

  # https://devenv.sh/services/
  # services.postgres.enable = true;

  # https://devenv.sh/scripts/
  scripts.hello.exec = ''
    echo hello from $GREET
  '';

  # https://devenv.sh/basics/
  enterShell = ''
    hello         # Run scripts directly
    git --version # Use packages
  '';

  # https://devenv.sh/tasks/
  # tasks = {
  #   "myproj:setup".exec = "mytool build";
  #   "devenv:enterShell".after = [ "myproj:setup" ];
  # };

  # https://devenv.sh/tests/
  enterTest = ''
    echo "Running tests"
    git --version | grep --color=auto "${pkgs.git.version}"
  '';

  # https://devenv.sh/git-hooks/
  # git-hooks.hooks.shellcheck.enable = true;

  # See full reference at https://devenv.sh/reference/options/
}
