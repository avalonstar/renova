import { injectGlobal } from 'styled-components';

import reboot from './reboot';

export const foundation = {};

export default () => injectGlobal`
  ${reboot}
`;
