# molecule_custom_docker

**Note**: This is an example of how to create custom drivers for Molecule. It is not upstream for any official Molecule drivers, there will be no further support. **Do not use this in production**

## Requirements
This section describes everything you need to start use of `custom_docker`:
- Access to Docker without `sudo`
- Python >= 3.10
- Molecule >= 5.0.1

### Installed collections
These collections will be installed automaticly during `dependency` stage:
- [`community.docker`](https://docs.ansible.com/ansible/latest/collections/community/docker/index.html) >= 3.4.6

## Getting started
1. Install driver via `pip`:
   ```bash
   pip install git+ssh://git@github.com:VorobevPavel-dev/molecule_custom_docker.git
   ```
2. Check if driver is available:
   ```bash
   > molecule drivers
   ──────────────────────
   custom_docker                                                                                                                                                                                                                        
   delegated
   ```
3. Create scenario using installed driver
   ```bash
   # default scenario
   molecule init scenario -d custom_docker

   # named scenario
   molecule init scenario -d custom_docker <scenario_name>
   ```
4. Start testing
   ```bash
   molecule test -s <scenario_name>
   ```

## Configuration
You can provide configuration for test resources in `molecule.yml` file of scenario:
- `name (str, Required)`: name of created platform
- `image (str, Required)`: Docker image to use. Example: `python`
- `tag (str, Required)`: tag of Docker image. Example: `3.10-slim-buster`
