{ pkgs }: {
  deps = [
    pkgs.python310Packages.pytest
    pkgs.python310Packages.requests
  ];
}