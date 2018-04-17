/* eslint-disable jsx-a11y/anchor-is-valid */

import React from 'react';
import { Link } from 'react-router-dom';

import styled from 'styled-components';

import logotype from './logotype.svg';

const Header = () => (
  <Wrapper>
    <Container>
      <Brand>
        <Link to="/">Renova</Link>
      </Brand>
    </Container>
  </Wrapper>
);

const Wrapper = styled.nav`
  display: grid;
  grid-template-columns: auto 960px auto;

  background: #cd163f;
  color: #636675;
`;

const Container = styled.div`
  grid-column: 2;
  padding: 1rem 0;
  align-items: center;

  display: flex;
  color: #fff;
`;

const Brand = styled.div`
  display: block;
  width: 96px;
  height: 40px;

  background-image: url(${logotype});
  background-size: cover;
  text-indent: -9999px;
`;

export default Header;
