/* eslint-disable jsx-a11y/anchor-is-valid */

import React from 'react';
import { Link } from 'react-router-dom';

import styled from 'styled-components';
import { Container } from 'layouts/Dashboard';

const Navigation = () => (
  <Wrapper>
    <Container>
      <Items>
        <Item>
          <StyledLink to="/dashboard">Dashboard</StyledLink>
        </Item>
        <Item>
          <StyledLink to="/characters">Characters</StyledLink>
        </Item>
        <Item>
          <StyledLink to="/storage">Storage</StyledLink>
        </Item>
        <Item>
          <StyledLink to="/database/items">Items</StyledLink>
        </Item>
        <Item>
          <StyledLink to="/database/monsters">Monsters</StyledLink>
        </Item>
      </Items>
    </Container>
  </Wrapper>
);

const Wrapper = styled.nav`
  display: grid;
  grid-template-columns: auto 960px auto;

  border-bottom: 1px solid #e4e6ec;
  color: #636675;
`;

const Items = styled.ul`
  display: flex;
  flex-wrap: wrap;
  padding-left: 0;
  margin-bottom: 0;
  list-style: none;
`;

const Item = styled.li`
  margin-bottom: 0;
  position: relative;

  & + & {
    margin-left: 1.25rem;
  }
`;

const StyledLink = styled(Link)`
  display: block;

  border: 0;
  color: inherit;
  padding: 1rem 0;
`;

export default Navigation;
